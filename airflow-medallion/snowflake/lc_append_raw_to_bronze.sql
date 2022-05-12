copy into {SNOWFLAKE_DATABASE}.{SNOWFLAKE_SCHEMA}.{SNOWFLAKE_BRONZE_TABLE}
        from @{SNOWFLAKE_STAGE}/{SRC_FILE}
        file_format = (format_name ={SNOWFLAKE_FILE_FORMAT})
        ON_ERROR = CONTINUE ;