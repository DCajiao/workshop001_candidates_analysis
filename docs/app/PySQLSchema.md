# 🐍🗒️ PySQLSchema

**PySQLSchema** is a Python library designed by [DCajiao](https://github.com/DCajiao) to facilitate the automatic generation of SQL schemas and seed data from pandas DataFrames. The library simplifies the process of converting your data stored in pandas into SQL queries that can be directly used to create and populate SQL tables.

## Features

- **Schema Generation**: Automatically generates SQL `CREATE TABLE` statements based on the structure of a pandas DataFrame.
- **Data Seeding**: Generates SQL `INSERT` statements to seed data from a pandas DataFrame into the corresponding SQL table.
- **Type Inference**: Automatically infers SQL data types (`INTEGER`, `FLOAT`, `BOOLEAN`, `TIMESTAMP`, `TEXT`) from pandas dtypes.
- **File Writing**: Outputs SQL queries to files, ensuring necessary directories are created.

## Usage

### 1. Import the Library

Start by importing the necessary modules and the `SQLSchemaGenerator` class.

```python
import pandas as pd
from pysqlschema import SQLSchemaGenerator
```

### 2. Create an Instance of `SQLSchemaGenerator`

You need to initialize the `SQLSchemaGenerator` with the name of the table for which you want to generate the schema and seed data.

```python
schema_generator = SQLSchemaGenerator(table_name='my_table')
```

### 3. Generate SQL Schema

Assuming you have a pandas DataFrame `df`, you can generate the SQL schema with the following:

```python
df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'created_at': pd.to_datetime(['2021-01-01', '2021-02-01', '2021-03-01'])
})

schema_generator.generate_schema(df)
```

This will generate a SQL `CREATE TABLE` statement and write it to `sql/schema.sql`. The default file path can be overridden:

```python
schema_generator.generate_schema(df, query_file_path='output/schema.sql')
```

If you need to get the SQL query string directly instead of writing it to a file, you can set `return_query=True`:

```python
schema_sql = schema_generator.generate_schema(df, return_query=True)
print(schema_sql)
```

### 4. Generate Seed Data

After generating the schema, you might want to insert the data from the DataFrame into the SQL table. This can be done as follows:

```python
schema_generator.generate_seed_data(df)
```

This will generate SQL `INSERT` statements and write them to `sql/seed_data.sql`. As with schema generation, the file path can be customized:

```python
schema_generator.generate_seed_data(df, query_file_path='output/seed_data.sql')
```

To get the SQL insert statements as a string instead of writing them to a file, use `return_query=True`:

```python
seed_data_sql = schema_generator.generate_seed_data(df, return_query=True)
print(seed_data_sql)
```

## Example

Below is a full example of how you might use PySQLSchema:

```python
import pandas as pd
from pysqlschema import SQLSchemaGenerator

# Create a sample DataFrame
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'created_at': pd.to_datetime(['2021-01-01', '2021-02-01', '2021-03-01'])
}

df = pd.DataFrame(data)

# Initialize the schema generator
schema_generator = SQLSchemaGenerator(table_name='users')

# Generate SQL schema
schema_generator.generate_schema(df, query_file_path='output/schema.sql')

# Generate seed data
schema_generator.generate_seed_data(df, query_file_path='output/seed_data.sql')
```

## Logging

The library uses Python’s built-in logging module to log information about the process, such as when a file is written or when SQL types are inferred. You can control the logging level via the `logging.basicConfig()` function.

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---