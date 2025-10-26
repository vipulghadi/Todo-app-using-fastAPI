from typing import Any,List
from fastapi.responses import JSONResponse

def api_response(status_code:int=200,
                 message:str="ok",
                 success:bool=True,
                 data:Any=None,
                 errors:List[Any]=None) -> JSONResponse:

    return JSONResponse(status_code=status_code,
                        content={
                            "message":message,
                            "success":success,
                            "data":data,
                            "errors": errors if errors is not None else []
                        })