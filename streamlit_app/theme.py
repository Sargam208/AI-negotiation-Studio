# =====================================
# theme.py
# =====================================

def load_theme():

    return """
    <style>

    .main {

        background:
        linear-gradient(
            135deg,
            #0f172a,
            #1e293b
        );

        color: white;
    }

    .hero {

        text-align: center;

        padding: 20px;

        border-radius: 20px;

        background:
        rgba(
            255,
            255,
            255,
            0.05
        );

        backdrop-filter:
        blur(10px);

        margin-bottom: 20px;
    }

    .metric-card {

        background:
        rgba(
            255,
            255,
            255,
            0.08
        );

        padding: 20px;

        border-radius: 18px;

        text-align: center;
    }

    </style>
    """