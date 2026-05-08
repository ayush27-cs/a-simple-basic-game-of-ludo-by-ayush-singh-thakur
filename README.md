flowchart TD
    A[Start Game] --> B[Roll Dice]
    B --> C{Is it 6?}
    C -- Yes --> D[Unlock Piece]
    C -- No --> E[Move Piece Forward]
    D --> F{Roll Again?}
    E --> F{Roll Again?}
    F -- Yes --> B
    F -- No --> G[End Game]
