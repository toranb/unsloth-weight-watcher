Analyze Mistral 7B fine tuning with weight watcher

### SFT with unsloth

```
git clone git@github.com:toranb/unsloth-weight-watcher.git analyze
cd analyze
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
mkdir yolo
# copy over model directory with full 7B mistral model
python3 demo.py
```
