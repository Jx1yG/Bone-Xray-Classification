{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import tensorflow as tf\n",
        "from tensorflow.keras import layers, models\n",
        "\n",
        "def build_model():\n",
        "    base_model = tf.keras.applications.ResNet50(input_shape=(224, 224, 3), include_top=False, weights='imagenet')\n",
        "    base_model.trainable = False  # Freeze pre-trained layers\n",
        "\n",
        "    # Build the CNN model\n",
        "    image_input = layers.Input(shape=(224, 224, 3))\n",
        "    x = base_model(image_input, training=False)\n",
        "    x = layers.GlobalAveragePooling2D()(x)\n",
        "    x = layers.Dense(256, activation='relu')(x)\n",
        "    x = layers.Dropout(0.5)(x)\n",
        "\n",
        "    abnormality_output = layers.Dense(1, activation='sigmoid', name='abnormality')(x)\n",
        "    body_part_output = layers.Dense(3, activation='softmax', name='body_part')(x)\n",
        "\n",
        "    model = models.Model(inputs=image_input, outputs=[abnormality_output, body_part_output])\n",
        "\n",
        "    return model"
      ],
      "metadata": {
        "id": "EoxKNSs3HLEd"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}