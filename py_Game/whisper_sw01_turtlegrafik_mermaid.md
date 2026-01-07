
```mermaid
flowchart 
    Q[Queue]
    T[turtle_thread]
   
    R[record_audio]
    M[Mikrofon]
    TG[Turtle Grafik]
    
    Q -- Kommando holen --> T
    M --> R
    W[whisper_thread]
    R -- Audio Aufnahme--> W
    W --> R
    W -- Kommando speichern --> Q
    
    T --> TG
    TG --> T

    classDef green fill:#BDFFA4,stroke:#2b8a3e;
    classDef amber fill:#FFDEAD,stroke:#e67e22;
    classDef red   fill:#FF9999,stroke:#c0392b;

    class W green;
    class R green;
    class T amber;
    class TG amber;
    class Q red;