import hashlib,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from artonelico_tool.iso import IsoEntry
from artonelico_tool.movie_pack import load_movie_pack, apply_movie_pack

class MoviePackTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]/'work');self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.pack=self.root/'videos_ptbr';self.pack.mkdir()
        self.iso=self.root/'base.iso';self.iso.write_bytes(bytes(8192))
        self.payload=b'\x00\x00\x01\xbaSofdecStream'+bytes(64)
        (self.pack/'test.SFD').write_bytes(self.payload)
        self.entry=IsoEntry('MOVIE/TEST.SFD',2,1024,False)
        self.item={'iso_path':self.entry.path,'file':'test.SFD','sha256':hashlib.sha256(self.payload).hexdigest(),'original_sha256':hashlib.sha256(bytes(1024)).hexdigest(),'validation':{'audio_unchanged':True,'frames_equal':True}}
        self.save()
    def save(self):
        (self.pack/'manifest.json').write_text(json.dumps({'schema':1,'movies':[self.item]}),encoding='utf8')
    def load(self):
        with patch('artonelico_tool.movie_pack.find',return_value=self.entry):
            return load_movie_pack(self.iso,self.pack)
    def test_valid(self):self.assertEqual(len(self.load()),1)
    def test_hash(self):
        self.item['sha256']='bad';self.save()
        with self.assertRaises(ValueError):self.load()
    def test_original_hash(self):
        self.item['original_sha256']='bad';self.save()
        with self.assertRaises(ValueError):self.load()
    def test_path_escape(self):
        self.item['file']='../test.SFD';self.save()
        with self.assertRaises(ValueError):self.load()
    def test_incomplete_pack(self):
        (self.pack/'manifest.json').unlink()
        with self.assertRaises(ValueError):self.load()
    def test_unvalidated(self):
        self.item['validation']['frames_equal']=False;self.save()
        with self.assertRaises(ValueError):self.load()
    def test_apply_and_padding(self):
        movies=self.load()
        new=IsoEntry(self.entry.path,2,len(self.payload),False)
        with patch('artonelico_tool.movie_pack.find',side_effect=[self.entry,new]),patch('artonelico_tool.movie_pack.move_iso_file_record') as move:
            result=apply_movie_pack(self.iso,movies)
        self.assertTrue(result[0]['reopened_verified']);move.assert_called_once()
        data=self.iso.read_bytes()
        self.assertEqual(data[4096:4096+len(self.payload)],self.payload)
        self.assertEqual(data[4096+len(self.payload):5120],bytes(1024-len(self.payload)))
