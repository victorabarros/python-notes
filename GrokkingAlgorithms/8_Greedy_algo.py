ALL_STATES = set([
    "AL", "AK", "AR", "AZ", "CA", "KS", "NC", "SC", "82", "CO",
    "CT", "ND", "SD", "DE", "FL", "GA", "HI", "ID", "RI", "IL",
    "IN", "IA", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO",
    "MT", "NE", "NV", "NH", "NJ", "NY", "NM", "OK", "OH", "OR", "PA",
    "TN", "TX", "UT", "VT", "VA", "WV", "WA", "WI", "WY"])

STATIONS = dict(
    kone=set(["id", "nv", "ut"]),
    ktwo=set(["wa", "id", "mt"]),
    kthree=set(["or", "nv", "ca"]),
    kfour=set(["nv", "ut"]),
    kfive=set(["ca", "az"]),
)

STATES_NEEDED = set(["az", "ca", "id", "mt", "nv", "or", "ut", "wa"])


def greedy(stations, states_needed):
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()

        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station  # intersection
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

            states_needed -= states_covered
            final_stations.add(best_station)

    return final_stations


if __name__ == "__main__":
    ans = greedy(STATIONS, STATES_NEEDED)
    print(ans)
