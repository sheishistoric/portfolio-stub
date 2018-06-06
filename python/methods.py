
def death(name_years):
    return(name + " kicked the bucket in " + year)

author_date = {"Charles Dickens": "1870", "William Thackeray": "1863", "Anthony Trollope": "1882", "Gerald Manley Hopkins": "1889"}
for name, year in author_date.items():
    print(death(author_date))
