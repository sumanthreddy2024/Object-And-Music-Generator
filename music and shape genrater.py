"""
Artistic Masterpiece Generator

This script generates a visual masterpiece and a harmonious musical composition based on user input.
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import music21
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_artistic_color():
    """
    Generate a random color for artistic expression.

    Returns:
        np.ndarray: A 3-element array representing the RGB values of the color.
    """
    logging.debug("Generating artistic color...")
    return np.random.rand(3,)

def create_vibrant_line(ax):
    """
    Draw a vibrant line on the given Axes.

    Args:
        ax (matplotlib.axes.Axes): The Axes object to draw on.
    """
    logging.debug("Creating vibrant line...")
    x = np.random.rand(2)
    y = np.random.rand(2)
    ax.plot(x, y, color=generate_artistic_color(), linewidth=np.random.uniform(0.5, 3))

def create_creative_circle(ax):
    """
    Draw a creative circle on the given Axes.

    Args:
        ax (matplotlib.axes.Axes): The Axes object to draw on.
    """
    logging.debug("Creating creative circle...")
    center = np.random.rand(2)
    radius = np.random.uniform(0.05, 0.2)
    circle = plt.Circle(center, radius, color=generate_artistic_color(), fill=True)
    ax.add_artist(circle)

def create_innovative_rectangle(ax):
    """
    Draw an innovative rectangle on the given Axes.

    Args:
        ax (matplotlib.axes.Axes): The Axes object to draw on.
    """
    logging.debug("Creating innovative rectangle...")
    width = np.random.uniform(0.05, 0.2)
    height = np.random.uniform(0.05, 0.2)
    lower_left = np.random.rand(2)
    rectangle = plt.Rectangle(lower_left, width, height, color=generate_artistic_color(), fill=True)
    ax.add_artist(rectangle)

def compose_harmonious_music(num_shapes, shape_types):
    """
    Generate a harmonious musical composition based on the art parameters.

    Args:
        num_shapes (int): The number of shapes to generate.
        shape_types (list): A list of shape types to use.

    Returns:
        music21.stream.Stream: The generated musical composition.
    """
    logging.info("Composing harmonious music...")
    composition = music21.stream.Stream()
    for _ in range(num_shapes):
        shape_type = random.choice(shape_types)
        if shape_type == 'line':
            note = music21.note.Note('C4', quarterLength=1)
        elif shape_type == 'circle':
            note = music21.note.Note('E4', quarterLength=1)
        elif shape_type == 'rectangle':
            note = music21.note.Note('G4', quarterLength=1)
        composition.append(note)
    composition.show('midi')

def create_visual_masterpiece(num_shapes, shape_types, art_size):
    """
    Generate and display a visual masterpiece.

    Args:
        num_shapes (int): The number of shapes to generate.
        shape_types (list): A list of shape types to use.
        art_size (tuple): The size of the artwork (width, height).
    """
    logging.info("Creating visual masterpiece...")
    fig, ax = plt.subplots(figsize=art_size)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    for _ in range(num_shapes):
        shape_type = random.choice(shape_types)
        if shape_type == 'line':
            create_vibrant_line(ax)
        elif shape_type == 'circle':
            create_creative_circle(ax)
        elif shape_type == 'rectangle':
            create_innovative_rectangle(ax)
    
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

def main():
    logging.info("Starting artistic masterpiece generator...")
    num_shapes = int(input("Enter the number of shapes: "))
    shape_types = input("Enter the shape types (line, circle, rectangle) separated by commas: ").split(',')
    shape_types = [shape.strip() for shape in shape_types]
    art_size = input("Enter the art size (e.g., 8,8): ")
    art_size = tuple(map(int, art_size.split(',')))
    compose_harmonious_music(num_shapes, shape_types)
    create_visual_masterpiece(num_shapes, shape_types, art_size)

if __name__ == "__main__":
    main()