"""
Some sample test cases for A Bard Day's Night.
Feel free to add more!

Notice that to efficiently create a Village,
we prepare a set of villagers and bards, a set of songs, and a list of parties,
and then pass make_file(v, s, p) to read_input.
"""

import pytest
from io import StringIO
from typing import TextIO
import bard


def make_file(villagers: list[str], songs: list[str], parties: list[str]) -> TextIO:
    v_str = "\n".join(villagers) + ("\n" if villagers else "")
    s_str = "\n".join(songs) + ("\n" if songs else "")
    p_str = "\n".join(parties) + ("\n" if parties else "")
    s = f"VILLAGERS\n{v_str}\nSONGS\n{s_str}\nPARTIES\n{p_str}"
    return StringIO(s)


# Holders for constants to avoid changing them between tests
CONSTANTS = {"BARD_THRESHOLD": None, "BILLBOARD_N": None}


def setup_function() -> None:
    """Hang on to the module's original constants before running any test."""
    CONSTANTS["BARD_THRESHOLD"] = bard.BARD_THRESHOLD
    CONSTANTS["BILLBOARD_N"] = bard.BILLBOARD_N


def teardown_function() -> None:
    """Restore the module's original constants after running any test."""
    bard.BARD_THRESHOLD = CONSTANTS["BARD_THRESHOLD"]
    bard.BILLBOARD_N = CONSTANTS["BILLBOARD_N"]


def test_read_input() -> None:
    """Test whether read_input reads input correctly."""
    villagers = {"Damien Rice", "Drake*"}
    songs = {"Rule, Britannia"}
    parties = ["Damien Rice,Drake", "Damien Rice"]

    v, b, s, p = bard.read_input(make_file(villagers, songs, parties))

    assert {"Damien Rice"} == set(v)
    assert {"Drake"} == b

    assert {"Rule, Britannia"} == set(s)


def test_unheard_songs() -> None:
    """Test whether unheard_songs returns the right songs."""
    villagers = {"Drake", "Damien Rice*"}
    songs = {"Call Me Maybe", "Lonely", "Square Enix Medley"}
    parties = ["Damien Rice,Drake", "Drake"]

    v, b, s, p = bard.read_input(make_file(villagers, songs, parties))
    for party in p:
        bard.sing_at_party(v, b, s, party)
        bard.update_bards_after_party(v, b, s, party)

    assert {"Lonely", "Square Enix Medley"} == bard.unheard_songs(v, b, s, p)


def test_all_bards() -> None:
    """Test whether all_bards is right when one Villager changes status."""
    villagers = {"Rabbit Peter*", "Haase Jakob", "Marty*"}
    songs = {"That Lucky Old Sun", "All I Want for Christmas Is You"}
    parties = ["Rabbit Peter,Haase Jakob", "Haase Jakob,Marty"]

    bard.BARD_THRESHOLD = 2

    v, b, s, p = bard.read_input(make_file(villagers, songs, parties))
    for party in p:
        bard.sing_at_party(v, b, s, party)
        bard.update_bards_after_party(v, b, s, party)

    assert {"Rabbit Peter", "Haase Jakob", "Marty"} == bard.all_bards(v, b, s, p)


def test_handout_example() -> None:
    """Test all aspects of the example given in the handout."""

    with open("handout_example.txt", "r") as f:
        v, b, s, p = bard.read_input(f)

    for party in p:
        bard.sing_at_party(v, b, s, party)
        bard.update_bards_after_party(v, b, s, party)

    assert {"What a Man Gotta Do", "People, I've Been Sad"} == bard.unheard_songs(
        v, b, s, p
    )

    assert [
        "Call Me Maybe",
        "Delete Forever",
        "People, I've Been Sad",
        "What a Man Gotta Do",
    ] == bard.billboard_top(v, b, s, p)

    assert {"Dan Zingaro"} == bard.all_bards(v, b, s, p)

    avg_ats = bard.average_attendees(v, b, s, p)

    assert isinstance(avg_ats, int)
    assert avg_ats == 3


if __name__ == "__main__":

    pytest.main(["test_bard.py"])
