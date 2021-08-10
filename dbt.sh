# install dbt: https://docs.getdbt.com/dbt-cli/installation
pip install dbt==0.20.0

# clone repo
git clone https://github.com/dbt-labs/jaffle_shop

# create ~/.dbt/profiles.yml

# ensure profile setup
dbt debug

# load demo data
dbt seed

# run models
dbt run

# test models
dbt test

# Generate docs
dbt docs generate

# View docs
dbt docs serve
