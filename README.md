# Streamlit & Dash Insights Project

A comprehensive data insights and visualization project built with Streamlit and Dash frameworks.

## 🚀 Project Overview

This project provides interactive data visualization and insights through both Streamlit and Dash applications, offering different user experiences for data exploration and analysis.

## 📁 Project Structure

```
Streamlit_Dash_Deploy/
├── Data/                    # Data storage
│   ├── raw/                # Raw data files
│   ├── processed/          # Cleaned and processed data
│   ├── external/           # External data sources
│   ├── interim/            # Intermediate data files
│   └── results/            # Output and results
├── src/                    # Source code
│   ├── streamlit/          # Streamlit application files
│   ├── dash/               # Dash application files
│   ├── utils/              # Utility functions
│   ├── config/             # Configuration files
│   ├── models/             # Data models and ML models
│   └── components/         # Reusable UI components
├── tests/                  # Unit and integration tests
├── docs/                   # Project documentation
├── notebooks/              # Jupyter notebooks
├── cursorrules/            # Cursor interaction rules
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Streamlit_Dash_Deploy
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Streamlit Application
```bash
cd src/streamlit
streamlit run app.py
```

### Dash Application
```bash
cd src/dash
python app.py
```

## 📊 Features

- **Interactive Dashboards**: Real-time data visualization
- **Data Processing**: Automated data cleaning and transformation
- **Machine Learning**: Predictive analytics and insights
- **Responsive Design**: Mobile-friendly interfaces
- **Custom Components**: Reusable UI elements

## 🧪 Testing

Run tests using pytest:
```bash
pytest tests/
```

## 📝 Documentation

- Check the `docs/` folder for detailed documentation
- Jupyter notebooks in `notebooks/` for data exploration
- Cursor rules in `cursorrules/` for UI interaction guidelines

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions, please open an issue in the repository. 