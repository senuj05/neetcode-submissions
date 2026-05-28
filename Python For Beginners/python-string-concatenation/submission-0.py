def concatenate(s1: str, s2: str) -> str:
    final_string = s1 + s2
    if (len(final_string) > 10):
        return "Too long!"
    else:
        return final_string




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
