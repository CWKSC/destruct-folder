import cv2
import numpy as np
import torch
import torchvision.transforms as transforms

def convertCv2ImageToTorchModelInputTensor(image: np.ndarray) -> torch.Tensor:
    # print("test: ", image.shape)
    imageResized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_CUBIC)
    transformer = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    return torch.unsqueeze(transformer(imageResized), 0)

def cropByRect(image: np.ndarray, top: int, bottom: int, left: int, right: int) -> np.ndarray:
    return image[top : bottom, left : right]


def BGRtoRGB(image: np.ndarray):
    """
    image is BGR image
    """
    return image[:, :, ::-1]

def RGBtoBGR(image: np.ndarray):
    """
    image is RGB image
    """
    return image[:, :, ::-1]

def readRGBImage(imagePath: str) -> np.ndarray:
    return cv2.imread(imagePath)[:, :, ::-1]


def writeRGBImage(path: str, image: np.ndarray):
    """
    image is RGB image
    """
    cv2.imwrite(path, image[:, :, ::-1])

def showRGBImage(image: np.ndarray):
    """
    image is RGB image
    """
    cv2.imshow("image", RGBtoBGR(image))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showGrayImage(image: np.ndarray):
    """
    image is gray image
    """
    cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
