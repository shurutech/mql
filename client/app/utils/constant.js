export const COMMAND_DOWNLOAD_SCRIPT =
  "curl -o script.sh https://storage.googleapis.com/analytics-script-bucket/extract_schema.sh";
export const COMMAND_RUN_SCRIPT = `chmod +x ./script.sh && ./script.sh <database_name> <username> <output_filename(optional)>`;