
class QueryService:
    def convert_to_2d_array(self,json_data):
        column_names = []

        rows = []

        for row_data in json_data:
            if not column_names:
                column_names = list(row_data.keys())

            row_values = [row_data[column_name] for column_name in column_names]
            rows.append(row_values)

        result = {
                'column_names': column_names,
                'rows': rows
        }

        return result



query_service = QueryService()