5-mlops-python-for-ml-project/
├── .gitignore
├── .python-version
├── create_mlops_structure.py    # Temporary script (can be deleted)
├── LICENSE
├── main.py                      # Entry point
├── pyproject.toml              # Project configuration
├── README.md
├── .venv/                      # Virtual environment
│   ├── Lib/site-packages/
│   └── Scripts/
└── src/                        # Main package directory
    ├── components/             # ML pipeline components
    │   ├── __init__.py
    │   ├── data_ingestion.py
    │   ├── data_validation.py
    │   ├── data_transformation.py
    │   └── model_trainer.py
    ├── constants/              # Configuration constants
    │   └── __init__.py
    ├── exception/              # Custom exceptions
    │   └── __init__.py
    ├── logging/                # Logging configuration
    │   └── __init__.py
    └── utils/                  # Utility functions
        └── __init__.py