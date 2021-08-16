def make_shirt(shirt_size="large",shirt_text="I love Python"):
    print(f"The size of the shirt is {shirt_size},and the text of the shirt is '{shirt_text}'")
make_shirt("Medium","Using positional argument")
make_shirt()
make_shirt("medium")
make_shirt("small","I like javascript")
make_shirt(shirt_size="small",shirt_text="Using keyword argument")