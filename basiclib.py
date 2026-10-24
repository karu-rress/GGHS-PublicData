class otd:
    @staticmethod
    def rm_duplicate(lt: list) -> list:
        return list(set(lt))

    @staticmethod
    def sort_dict(dict: dict, is_ascending: bool=True) -> dict:
        if is_ascending:
            return {k: v for k, v in sorted(dict.items(), key=lambda x: -x[1])}
        else:
            return {k: v for k, v in sorted(dict.items(), key=lambda x: x[1])}
