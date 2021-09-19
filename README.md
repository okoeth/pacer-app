# Environment Setup

To set-up the environment run:

```
conda env create -f environment.yml
pip install -r requirements.txt
. ./set-env.sh
```

To run the app:

```
flask run
```

To test the app use:

```
# Test for basic health
curl \
    --location \
    --request GET 'http://localhost:5000/info'

# Test referemce file upload
curl \
    --location \
    --request POST 'http://localhost:5000/upload-reference' \
    --form 'reference_file=@"./data/wank_reference.gpx"'
```