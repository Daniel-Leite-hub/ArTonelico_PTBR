import data_067_batch1 as b1
import data_067_batch2 as b2
import data_067_batch3 as b3

all_data = {}
all_data.update(b1.curated_dict)
all_data.update(b2.curated_dict)
all_data.update(b3.curated_dict)

for lid, info in sorted(all_data.items()):
    pt = info['pt']
    parts = pt.split('\n')
    for p in parts[1:]:
        if p.strip() and p.strip()[0] in '.,!?;:-—':
            print(f"Warning in {lid}: line starts with punctuation: {repr(p)}")
