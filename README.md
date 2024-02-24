Analyze Mistral 7B fine tuning with weight watcher

### Run after SFT with unsloth

```
git clone git@github.com:toranb/unsloth-weight-watcher.git analyze
cd analyze
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
# copy over model directory 7B mistral fine tune
# copy over base directory 7B mistral base model
python3 demo.py
```
