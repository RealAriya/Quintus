### Setting Up PostgreSQL

1. Install PostgreSQL on your machine.
2. Create a new PostgreSQL database:
    ```bash
    createdb Quintus
    ```
3. Import the database dump:
    ```bash
    psql -U David -h localhost -d Quintus -f quintus_dump.sql
    ```
4. Update the `settings.py` file with your PostgreSQL credentials.
