from gamayun.gamayun_utils import report_result
from gamayun.gamayun_utils import report_error
from gamayun.gamayun_utils import run_gamayun_script_logic


def job_logic():
    report_result(["first result", "second result", "third result"])


run_gamayun_script_logic(job_logic)
