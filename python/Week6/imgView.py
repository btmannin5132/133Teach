import matplotlib.pyplot as plt

# Prompt user for image name​
image_name = input('Enter image name (with extension): ')
# Read the image using matplotlib​
image = plt.imread(image_name)

# Display the image​
plt.figure()
plt.imshow(image)
plt.title('Spider Pete')
plt.xlabel('It is a spider')  # Appropriate label
plt.ylabel('It is Pete')  # Appropriate label if needed

# Show the plot​

plt.show()