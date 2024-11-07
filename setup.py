from setuptools import setup, find_packages

setup(
    name="dsss_homework_2",              # 项目名称
    version="0.1.0",                     # 项目版本
    author="Dexiao Zhou",                # 作者
    author_email="your.email@example.com",  # 作者邮箱
    description="A description of the project",  # 简短描述
    long_description=open("README.md").read(),   # 详细描述
    long_description_content_type="text/markdown",
    url="https://github.com/Dexiao-Zhou/dsss_homework_2",  # 项目主页
    packages=find_packages(),            # 自动查找项目中的包
    install_requires=[                   # 项目依赖
        "requests>=2.25.1",              # 示例依赖项，修改为你的实际依赖
        "numpy>=1.19.0",
    ],
    classifiers=[                        # 项目分类
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)