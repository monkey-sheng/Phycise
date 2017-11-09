def PrintDiagram(path):
    from PIL import Image
    import matplotlib.pyplot as plt
    img=Image.open(path)
    plt.figure("diagram")
    plt.imshow(img)
    plt.axis("off")
    plt.show()
