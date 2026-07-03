def markdown_to_html(markdown):
    if markdown.startswith("# "):
        return f"<h1>{markdown[2:]}</h1>"

    elif markdown.startswith("**") and markdown.endswith("**"):
        return f"<b>{markdown[2:-2]}</b>"

    else:
        return markdown


while True:
    print("\n===== MARKDOWN TO HTML CONVERTER =====")
    print("1. Convert Markdown")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        markdown_text = input("Enter Markdown Text: ")
        html_output = markdown_to_html(markdown_text)

        print("\nConverted HTML:")
        print(html_output)

    elif choice == "2":
        print("Thank you for using Markdown to HTML Converter!")
        break

    else:
        print("Invalid Choice! Please try again.")