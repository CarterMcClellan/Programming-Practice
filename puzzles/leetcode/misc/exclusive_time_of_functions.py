from dataclasses import dataclass

@dataclass
class Log:
    id: int
    state: str
    time: int
    is_start: bool

def parse_log(log: str) -> Log:
    [id, state, time] = log.split(":")
    return Log(
        id=int(id),
        state=state,
        time=int(time),
        is_start=(state=="start")
    )

class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result = [0 for _ in range(n)]
        active_procs = []

        for log in logs:
            curr_proc = parse_log(log)
            if curr_proc.is_start:
                active_procs.append(curr_proc)
            else:
                start_proc = active_procs.pop(-1)
                total_time = (curr_proc.time - start_proc.time) + 1
                result[curr_proc.id] += total_time

                # problem: if a program branches, we don't want to include
                # that old time in the new time so we actually just subtract that time
                if len(active_procs) >= 1:
                    result[active_procs[-1].id] -= total_time

        return result


# Analsis
# 1) If we know the total runtime of the program we might be able to bound the total time for any process
#    and use some kind of bit packing tecnique
#
# 2) Worst case we keep starting processes and not ending any so the active procs array gets long, in that case
#    we could store only then active process ids on the stack, then store the metadata (like time and state)
#    in a on disk key value store
#
# 3) Lets think through how we would want to make this solution work better in a multi-threaded environment... I
#    think that functionally we could reuse this class for each individual thread, but have a wrapper which instantiated
#    new instances based on the logger which was being used.
#
# 4) Within the control flow we could think through things like "interrups" and "exceptions" the same way we handle program end statements.