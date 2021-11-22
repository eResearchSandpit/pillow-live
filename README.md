# This is the repo for the live python image manipulation workshop at ResBaz 2021

We'll be adding to this repo as the session progresses.  If you have git setup you can clone this repo to follow along with us if you'd like.


Clone this repo like so
```bash
git@github.com:eResearchSandpit/pillow-live.git
```

Then when we push changes you can download them with

```bash
git pull
```

The dataset I used in the session is from [LILA BC](https://lila.science/image-access)

To use the same images:
Use [Azure Copy](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) to download sample image dataset from [LILA BC](https://lila.science/image-access)
```bash
azcopy cp "https://lilablobssc.blob.core.windows.net/missouricameratraps/images/Set1/1.02-Agouti/SEQ75520?st=2020-01-01T00%3A00%3A00Z&se=2034-01-01T00%3A00%3A00Z&sp=rl&sv=2019-07-07&sr=c&sig=zf5Vb3BmlGgBKBM1ZtAZsEd1vZvD6EbN%2BNDzWddJsUI%3D" . --recursive
azcopy cp "https://lilablobssc.blob.core.windows.net/missouricameratraps/images/Set1/1.02-Agouti/SEQ75583?st=2020-01-01T00%3A00%3A00Z&se=2034-01-01T00%3A00%3A00Z&sp=rl&sv=2019-07-07&sr=c&sig=zf5Vb3BmlGgBKBM1ZtAZsEd1vZvD6EbN%2BNDzWddJsUI%3D" . --recursive
```