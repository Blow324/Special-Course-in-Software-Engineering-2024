name = "Charles Dickens"
born = "February 7, 1812"
born_place = "Portsmouth, England"
occupation = "English novelist"
famous_works = "A Christmas Carol, Oliver Twist, David Copperfield, Great Expectations"
married = "Catherine Hogarth"
marriage_year = 1836
children = 10
talent = "dramatic public readings"
died = "June 9, 1870"
died_place = "Gad’s Hill Place, Kent, England"



# Extracting 'C' from the name

initial = name.split()[0][0]  # 'C' from Charles Dickens

# Forming the multiline string output
output_text = f"""A Brief Profile of {initial}. Dickens in {{}} characters.
Hello. My name is {name}. I am an {occupation}. I was born on {born}, in {born_place}. I am most famous as a writer of the Victorian era. I married {married} in {marriage_year}. We have {children} children. Some of my most famous works include “{famous_works.replace(', ', ',” “')}.” Besides being a writer, my other talent was doing {talent} of my work. I died on {died}, at my home in {died_place}."""

# Calculate the total length of the output text
total_chars = len(output_text.format(''))

# Update the output text with the correct character count
output_text = output_text.format(total_chars)

# Testing if the output matches the expected result
test_text = """A Brief Profile of C. Dickens in 508 characters.
Hello. My name is Charles Dickens. I am an English novelist. I was born on February 7, 1812, in Portsmouth, England. I am most famous as a writer of the Victorian era. I married Catherine Hogarth in 1836. We have ten children. Some of my most famous works include “A Christmas Carol,” “Oliver Twist,” “David Copperfield,” and “Great Expectations.” Besides being a writer, my other talent was doing dramatic public readings of my work. I died on June 9, 1870, at my home in Gad’s Hill Place, Kent, England."""

# Output and test the result
print(output_text)
print(output_text == test_text)  # This should return True if everything is correct
