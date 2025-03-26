def main():
  file_name = input("File name: ").strip().lower()
  mime_type = get_mime_type(file_name)
  print(mime_type)


def get_file_ext(file_name):
  name_parts = file_name.split(".")
  return name_parts[-1] if len(name_parts) > 1 else None


def get_mime_type(file_name):
  extension = get_file_ext(file_name)
  match extension:
    case "jpg" | "jpeg":
      return "image/jpeg"
    case "gif":
      return "image/gif"
    case "png":
      return "image/png"
    case "pdf":
      return "application/pdf"
    case "txt":
      return "text/plain"
    case "zip":
      return "application/zip"
    case _:
      return "application/octet-stream"


main()
