# Architecture Diagrams

This document contains all the Mermaid diagrams for the Streamlit & Dash Insights Project.

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph "Data Layer"
        A[Raw Data<br/>test.csv<br/>80MB, 310 cols]
        B[Processed Data]
        C[External Data]
        D[Results]
    end
    
    subgraph "Core Services"
        E[DataLoader<br/>File Operations]
        F[FinancialDataAnalyzer<br/>Domain Analysis]
        G[Configuration<br/>Settings Management]
    end
    
    subgraph "Application Layer"
        H[Streamlit App<br/>Rapid Prototyping]
        I[Dash App<br/>Advanced Interactivity]
    end
    
    subgraph "Visualization Layer"
        J[Plotly Charts]
        K[Interactive Graphs]
        L[Real-time Metrics]
    end
    
    subgraph "User Interface"
        M[Web Browser]
        N[Mobile Interface]
    end
    
    A --> E
    E --> F
    F --> G
    G --> H
    G --> I
    H --> J
    I --> K
    J --> L
    K --> L
    L --> M
    L --> N
    
    style A fill:#e1f5fe
    style E fill:#f3e5f5
    style F fill:#f3e5f5
    style H fill:#e8f5e8
    style I fill:#e8f5e8
    style J fill:#fff3e0
    style K fill:#fff3e0
```

## 📊 Data Flow Diagram

```mermaid
flowchart LR
    subgraph "Input"
        A[test.csv<br/>Financial Data]
    end
    
    subgraph "Processing"
        B[DataLoader<br/>Load & Validate]
        C[FinancialDataAnalyzer<br/>Analyze & Transform]
        D[Configuration<br/>Settings & Paths]
    end
    
    subgraph "Analysis"
        E[Gender Distribution]
        F[Income Analysis]
        G[Loan Amounts]
        H[Geographic Data]
        I[Application Status]
    end
    
    subgraph "Output"
        J[Streamlit Dashboard]
        K[Dash Dashboard]
        L[Visualizations]
        M[Real-time Metrics]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    D --> F
    D --> G
    D --> H
    D --> I
    E --> J
    F --> J
    G --> J
    H --> J
    I --> J
    E --> K
    F --> K
    G --> K
    H --> K
    I --> K
    J --> L
    K --> L
    L --> M
```

## 📁 Project Structure

```mermaid
graph TD
    A[Streamlit_Dash_Deploy] --> B[Data]
    A --> C[src]
    A --> D[tests]
    A --> E[docs]
    A --> F[notebooks]
    A --> G[cursorrules]
    A --> H[venv]
    
    B --> B1[raw]
    B --> B2[processed]
    B --> B3[external]
    B --> B4[interim]
    B --> B5[results]
    
    C --> C1[streamlit]
    C --> C2[dash]
    C --> C3[utils]
    C --> C4[config]
    C --> C5[models]
    C --> C6[components]
    
    C1 --> C1A[app.py]
    C2 --> C2A[app.py]
    C3 --> C3A[data_loader.py]
    C3 --> C3B[data_analyzer.py]
    C4 --> C4A[settings.py]
    
    D --> D1[test_data_loader.py]
    E --> E1[README.md]
    E --> E2[API_Documentation.md]
    E --> E3[Project_Setup_Documentation.md]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
    style E fill:#cc99ff
```

## 🔄 Development Workflow

```mermaid
graph LR
    subgraph "Development Phase"
        A[Project Setup]
        B[Core Development]
        C[Application Development]
        D[Testing]
    end
    
    subgraph "Deployment Phase"
        E[Environment Setup]
        F[Data Integration]
        G[Application Launch]
        H[Monitoring]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#f1f8e9
    style G fill:#e0f2f1
    style H fill:#fafafa
```

## 🎯 Component Interaction

```mermaid
sequenceDiagram
    participant U as User
    participant S as Streamlit App
    participant D as DataLoader
    participant F as FinancialDataAnalyzer
    participant C as Configuration
    participant V as Visualizations
    
    U->>S: Access Dashboard
    S->>C: Load Settings
    C->>S: Return Configuration
    
    S->>D: Load Data
    D->>S: Return DataFrame
    
    S->>F: Analyze Data
    F->>S: Return Analysis Results
    
    S->>V: Create Charts
    V->>S: Return Visualizations
    
    S->>U: Display Dashboard
    
    Note over U,V: Real-time interaction
    U->>S: Filter/Update
    S->>F: Re-analyze
    F->>S: Updated Results
    S->>U: Updated Display
```

## 📈 Data Processing Pipeline

```mermaid
flowchart TD
    A[Raw CSV File] --> B[Data Validation]
    B --> C{Valid?}
    C -->|Yes| D[Load into DataFrame]
    C -->|No| E[Error Handling]
    
    D --> F[Data Cleaning]
    F --> G[Missing Value Check]
    G --> H[Data Type Conversion]
    H --> I[Feature Engineering]
    
    I --> J[Analysis Modules]
    J --> K[Gender Analysis]
    J --> L[Income Analysis]
    J --> M[Loan Analysis]
    J --> N[Geographic Analysis]
    
    K --> O[Metrics Calculation]
    L --> O
    M --> O
    N --> O
    
    O --> P[Dashboard Display]
    P --> Q[Real-time Updates]
    
    style A fill:#e1f5fe
    style O fill:#e8f5e8
    style P fill:#fff3e0
    style E fill:#ffebee
```

## 🔧 Technology Stack

```mermaid
graph TB
    subgraph "Frontend"
        A[Streamlit]
        B[Dash]
        C[HTML/CSS]
        D[Bootstrap]
    end
    
    subgraph "Backend"
        E[Python 3.8+]
        F[Pandas]
        G[Numpy]
        H[Plotly]
    end
    
    subgraph "Data Processing"
        I[DataLoader]
        J[FinancialDataAnalyzer]
        K[Configuration]
    end
    
    subgraph "Development Tools"
        L[Git]
        M[VS Code]
        N[Pytest]
        O[Black]
    end
    
    subgraph "Deployment"
        P[Virtual Environment]
        Q[Requirements.txt]
        R[Local Server]
    end
    
    A --> E
    B --> E
    E --> F
    E --> G
    E --> H
    F --> I
    G --> J
    H --> K
    
    style A fill:#ff9999
    style B fill:#ff9999
    style E fill:#99ccff
    style F fill:#99ccff
    style G fill:#99ccff
    style H fill:#99ccff
```

## 🎨 User Interface Flow

```mermaid
graph TD
    A[Landing Page] --> B{Choose Application}
    B -->|Streamlit| C[Streamlit Dashboard]
    B -->|Dash| D[Dash Dashboard]
    
    C --> E[Overview Page]
    C --> F[Data Analysis Page]
    C --> G[Visualizations Page]
    C --> H[Predictions Page]
    C --> I[Settings Page]
    
    D --> J[Overview Tab]
    D --> K[Data Analysis Tab]
    D --> L[Visualizations Tab]
    D --> M[Predictions Tab]
    D --> N[Settings Tab]
    
    E --> O[Real-time Metrics]
    F --> P[Detailed Analysis]
    G --> Q[Interactive Charts]
    H --> R[ML Models]
    I --> S[Configuration]
    
    J --> O
    K --> P
    L --> Q
    M --> R
    N --> S
    
    style A fill:#e1f5fe
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style O fill:#f3e5f5
    style P fill:#f3e5f5
    style Q fill:#f3e5f5
```

## 🔍 Testing Strategy

```mermaid
graph LR
    subgraph "Unit Testing"
        A[DataLoader Tests]
        B[Analyzer Tests]
        C[Utility Tests]
    end
    
    subgraph "Integration Testing"
        D[App Integration]
        E[Data Flow Tests]
        F[API Tests]
    end
    
    subgraph "End-to-End Testing"
        G[User Workflow]
        H[Performance Tests]
        I[UI Tests]
    end
    
    A --> D
    B --> D
    C --> D
    D --> G
    E --> H
    F --> I
    
    style A fill:#e1f5fe
    style D fill:#e8f5e8
    style G fill:#fff3e0
```

---

**Note**: These diagrams can be rendered in any Markdown viewer that supports Mermaid syntax, such as GitHub, GitLab, or VS Code with the Mermaid extension. 