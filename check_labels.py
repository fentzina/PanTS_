#!/bin/bash
set -e

PanTSMini_Label_URL=http://www.cs.jhu.edu/~zongwei/dataset/PanTSMini_Label.tar.gz

cd data/

# Download PanTSMini_Label.tar.gz (Required to get the archive)
echo "Downloading PanTSMini_Label.tar.gz..."
wget --show-progress -O PanTSMini_Label.tar.gz "$PanTSMini_Label_URL"

echo "Extracting only the first 100 folders..."
mkdir -p LabelAll

# Generate exact list of the first 100 folders to extract
# This formats numbers 1 to 100 into the PanTS_0000XXXX pattern
extract_list=()
for i in {1..100}; do
    extract_list+=($(printf "PanTS_%08d" $i))
done

# Extract ONLY the specified 100 folders from the tar.gz archive
tar -xzf PanTSMini_Label.tar.gz -C LabelAll "${extract_list[@]}"

# Clean up the compressed archive
rm PanTSMini_Label.tar.gz

mkdir -p LabelTr
mkdir -p LabelTe

echo "Moving the extracted 100 training labels..."
cd LabelAll
# Since we only extracted 100 files, we can move them safely in one go
find . -maxdepth 1 -type d -name 'PanTS_0000*' -print0 | xargs -0 -r mv -t ../LabelTr/
cd ..

rmdir LabelAll 2>/dev/null || true

cd ..
