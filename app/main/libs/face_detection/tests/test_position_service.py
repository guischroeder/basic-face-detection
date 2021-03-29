import pytest

from collections import OrderedDict

from app.main.libs.face_detection.positions_service import PositionsService


positions_service = PositionsService()


def test_get_bounding_boxes_positions(data):
    result = [
        OrderedDict(
            [
                ("x", 220.88422775268555),
                ("y", 310.2390766143799),
                ("width", 54.85354661941528),
                ("height", 72.71535992622375),
            ]
        ),
        OrderedDict(
            [
                ("x", 32.182860374450684),
                ("y", 600.0266075134277),
                ("width", 52.74847149848938),
                ("height", 73.42749238014221),
            ]
        ),
        OrderedDict(
            [
                ("x", 432.7812671661377),
                ("y", 701.499080657959),
                ("width", 50.24377703666687),
                ("height", 74.42926168441772),
            ]
        ),
    ]

    assert positions_service.get_bounding_boxes_positions(data) == result


def test_get_bounding_boxes_positions_fail():
    with pytest.raises(Exception, match="Can't get bounding boxes positions"):
        positions_service.get_bounding_boxes_positions({})


def test_find_positions(data):
    result = [[2, 3], [0, 6], [4, 7]]

    assert positions_service.find_positions(data) == result


def test_find_positions_with_no_bounding_boxes(mocker, data_with_no_bouding_boxes):
    get_bounding_boxes_positions = mocker.spy(
        positions_service, "get_bounding_boxes_positions"
    )

    assert len(positions_service.find_positions(data_with_no_bouding_boxes)) == 0
    assert get_bounding_boxes_positions.spy_return == []
