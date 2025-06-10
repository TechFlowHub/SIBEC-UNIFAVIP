import pandas as pd

class CoordinatorControler:
    def __init__(self, root, connection):
        self.root = root
        self.conn = connection
        # The cursor is best created per execution to ensure thread safety
        # and prevent issues with stale cursors.

    def get_aggregated_data(self, group_by_column, filters=None, limit=None):
        """
        Fetches and aggregates scholarship data based on specified columns and filters.

        Args:
            group_by_column (str): The column to group the data by (e.g., 'race', 'course').
            filters (dict, optional): A dictionary of filters to apply (e.g., {'gender': 'Feminino'}).
                                      Defaults to None.
            limit (int, optional): The maximum number of records to return. Defaults to None.

        Returns:
            pd.DataFrame: A DataFrame with the aggregated data.
        """
        query = f"""
            SELECT {group_by_column}, COUNT(*) as count
            FROM scholarship
        """
        
        params = []
        if filters:
            # Add a WHERE clause if filters are provided
            where_clauses = []
            for key, value in filters.items():
                where_clauses.append(f"{key} = %s")
                params.append(value)
            query += " WHERE " + " AND ".join(where_clauses)
            
        query += f" GROUP BY {group_by_column} ORDER BY count DESC"
        
        if limit:
            query += f" LIMIT {int(limit)}" # Use int() for safety, though not for values

        # Use a new cursor for each execution
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        
        return pd.DataFrame(result) if result else pd.DataFrame(columns=[group_by_column, 'count'])

    def get_distinct_values(self, column):
        """Fetches distinct values for a given column to populate filters."""
        query = f"SELECT DISTINCT {column} FROM scholarship ORDER BY {column}"
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return result