import pytest


@pytest.fixture
def data():
    return {
        "FaceDetails": [
            {
                "BoundingBox": {
                    "Width": 0.0685669332742691,
                    "Height": 0.0908941999077797,
                    "Left": 0.27610528469085693,
                    "Top": 0.38779884576797485,
                },
            },
            {
                "BoundingBox": {
                    "Width": 0.06593558937311172,
                    "Height": 0.09178436547517776,
                    "Left": 0.040228575468063354,
                    "Top": 0.7500332593917847,
                },
            },
            {
                "BoundingBox": {
                    "Width": 0.06280472129583359,
                    "Height": 0.09303657710552216,
                    "Left": 0.5409765839576721,
                    "Top": 0.8768738508224487,
                },
            },
        ]
    }


@pytest.fixture
def data_with_no_bouding_boxes():
    return {"FaceDetails": []}
