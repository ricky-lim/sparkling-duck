# Sparkling Duck

This repository presents a performance comparison between Apache Spark and DuckDB for common data analysis tasks with equivalent query implementations using both tools.

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

# Install java 17
JAVA_VERSION=17.0.10-amzn
sdk install java $JAVA_VERSION
sdk use java $JAVA_VERSION
```

