# Download the Stanford MURA Dataset

This project uses the **Stanford MURA dataset**, which cannot be redistributed directly. Please follow the instructions below to download the dataset directly from the official source.

## Download Instructions

You can use the following code in your terminal or Jupyter notebook to download and unzip the dataset:

```bash
!wget "https://aimistanforddatasets01.blob.core.windows.net/muramskxrays/MURA-v1.1.zip?sv=2019-02-02&sr=b&sig=CRdz1%2B0mFZvv8KoAvw%2Ff24wS43Tw2CtRPrZKIXebg8E%3D&st=2024-09-27T04%3A29%3A20Z&se=2024-10-27T04%3A34%3A20Z&sp=r" -O MURA-v1.1.zip
!unzip MURA-v1.1.zip
```

## Important: Dataset License

The **Stanford MURA dataset** is subject to its own licensing terms and cannot be redistributed. By using this dataset, you agree to comply with the terms of the [MURA dataset license](https://stanfordaimi.azurewebsites.net/datasets/3e00d84b-d86e-4fed-b2a4-bfe3effd661b). Please review the license and ensure that your usage complies with the terms and conditions provided by Stanford.

## Dataset Usage Guidelines
- The dataset is provided for **non-commercial research purposes** only.
- Redistribution of the dataset is **not allowed**.
- You are responsible for obtaining permission from Stanford to use the dataset.

## How to Use the Downloaded Dataset

Once you have downloaded the dataset, place the contents into the following structure within your project directory:

```bash
/project-directory
└── data/
    └── MURA-v1.1/
        ├── train/
        ├── valid/
        └── ...
```
