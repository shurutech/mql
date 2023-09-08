export const CURL =
  "curl -o script.sh https://storage.googleapis.com/analytics-script-bucket/extract_schema.sh";
export const COMMAND = `chmod +x ./script.sh && ./script.sh <database_name> <username> <output_filename(optional)>`;
