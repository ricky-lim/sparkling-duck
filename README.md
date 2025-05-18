# Sparkling Duck

To explore sparkling-duck.py with vscode install `Jupyter` extension.

## Data origin

The data downloaded from `https://huggingface.co/datasets/Pablinho/movies-dataset/resolve/main/9000plus.csv`, converted to parquet format and saved as `data/moviews.parquet`.

## Install duckdb

As simple as `copy to` installation.

```
curl https://install.duckdb.org | sh
```

## Install pyspark

```
uv add pyspark

# Install java with sdkman
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# Install java 11
sdk install java 11.0.11.hs-adpt
sdk use java 11.0.11.hs-adpt 

# To automatically switch, edit the .sdkmanrc






```

