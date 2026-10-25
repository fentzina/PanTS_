# It only works on label files !!!
import os, csv
import numpy as np
import nibabel as nib

ROOT = '/content/drive/MyDrive/PanTS_paper'
rows = []

for dirpath, _, files in os.walk(ROOT):
    if 'pancreatic_lesion.nii.gz' in files:
        p = os.path.join(dirpath, 'pancreatic_lesion.nii.gz')
        try:
            n = int(np.count_nonzero(np.asanyarray(nib.load(p).dataobj)))
        except Exception as e:
            print(f'ERROR {p}: {e}')
            n = -1
        rows.append((dirpath, n))

print(f'Lesion files found: {len(rows)}')
print(f'With non-empty lesion: {sum(n > 0 for _, n in rows)}')
print(f'Unreadable: {sum(n < 0 for _, n in rows)}')

with open(os.path.join(ROOT, 'lesion_scan.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['case_dir', 'lesion_voxels'])
    w.writerows(sorted(rows, key=lambda r: -r[1]))
