from fastapi import APIRouter, Depends, status

from constants.response import common_error_authenticated_response
from controllers.requests import (get_server_status_requests_handler,
                                  get_download_requests_handler,
                                  get_delete_backup_requests_handler,
                                  delete_download_request_handler,
                                  delete_delete_backup_request_handler,
                                  delete_server_status_request_handler)
from schemas.request.delete_resource import DeleteResourceRequestSchema
from vui_common.schemas.response.successful_request import SuccessfulRequest
from vui_common.security.helpers.rate_limiter import RateLimiter, LimiterRequests

from vui_common.utils.swagger import route_description
from vui_common.utils.exceptions import handle_exceptions_endpoint

router = APIRouter()

tag_name = 'Requests'
endpoint_limiter = LimiterRequests(tags=tag_name,
                                   default_key='L1')

# ------------------------------------------------------------------------------------------------
#             GET SERVER STATUS REQUESTS
# ------------------------------------------------------------------------------------------------


limiter_restores = endpoint_limiter.get_limiter_cust("server_status_requests")
route = '/server-status-requests'


@router.get(
    path=route,
    tags=[tag_name],
    summary='Get server status requests',
    description=route_description(tag=tag_name,
                                  route=route,
                                  limiter_calls=limiter_restores.max_request,
                                  limiter_seconds=limiter_restores.seconds),
    dependencies=[Depends(RateLimiter(interval_seconds=limiter_restores.seconds,
                                      max_requests=limiter_restores.max_request))],
    response_model=SuccessfulRequest,
    responses=common_error_authenticated_response,
    status_code=status.HTTP_200_OK)
@handle_exceptions_endpoint
async def get_server_status_requests():
    return await get_server_status_requests_handler()


# ------------------------------------------------------------------------------------------------
#             GET DOWNLOAD REQUESTS
# ------------------------------------------------------------------------------------------------


limiter_restores = endpoint_limiter.get_limiter_cust("download_requests")
route = '/download-requests'


@router.get(
    path=route,
    tags=[tag_name],
    summary='Get download requests',
    description=route_description(tag=tag_name,
                                  route=route,
                                  limiter_calls=limiter_restores.max_request,
                                  limiter_seconds=limiter_restores.seconds),
    dependencies=[Depends(RateLimiter(interval_seconds=limiter_restores.seconds,
                                      max_requests=limiter_restores.max_request))],
    response_model=SuccessfulRequest,
    responses=common_error_authenticated_response,
    status_code=status.HTTP_200_OK)
@handle_exceptions_endpoint
async def get_download_requests():
    return await get_download_requests_handler()


# ------------------------------------------------------------------------------------------------
#             GET DELETE BACKUP REQUESTS
# ------------------------------------------------------------------------------------------------


limiter_restores = endpoint_limiter.get_limiter_cust("delete_backup_requests")
route = '/delete-backup-requests'


@router.get(
    path=route,
    tags=[tag_name],
    summary='Get download requests',
    description=route_description(tag=tag_name,
                                  route=route,
                                  limiter_calls=limiter_restores.max_request,
                                  limiter_seconds=limiter_restores.seconds),
    dependencies=[Depends(RateLimiter(interval_seconds=limiter_restores.seconds,
                                      max_requests=limiter_restores.max_request))],
    response_model=SuccessfulRequest,
    responses=common_error_authenticated_response,
    status_code=status.HTTP_200_OK)
@handle_exceptions_endpoint
async def get_delete_backup_requests():
    return await get_delete_backup_requests_handler()


# ------------------------------------------------------------------------------------------------
#             DELETE SERVER-STATUS-REQUEST
# ------------------------------------------------------------------------------------------------


limiter_restores = endpoint_limiter.get_limiter_cust("server_backup_request")
route = '/server-status-request'


@router.delete(
    path=route,
    tags=[tag_name],
    summary='Delete server-status-request',
    description=route_description(tag=tag_name,
                                  route=route,
                                  limiter_calls=limiter_restores.max_request,
                                  limiter_seconds=limiter_restores.seconds),
    dependencies=[Depends(RateLimiter(interval_seconds=limiter_restores.seconds,
                                      max_requests=limiter_restores.max_request))],
    response_model=SuccessfulRequest,
    responses=common_error_authenticated_response,
    status_code=status.HTTP_200_OK)
@handle_exceptions_endpoint
async def delete_server_status_request(request: DeleteResourceRequestSchema):
    return await delete_server_status_request_handler(request)


# ------------------------------------------------------------------------------------------------
#             DELETE DOWNLOAD-REQUEST
# ------------------------------------------------------------------------------------------------


limiter_restores = endpoint_limiter.get_limiter_cust("download_request")
route = '/download-request'


@router.delete(
    path=route,
    tags=[tag_name],
    summary='Delete download-request',
    description=route_description(tag=tag_name,
                                  route=route,
                                  limiter_calls=limiter_restores.max_request,
                                  limiter_seconds=limiter_restores.seconds),
    dependencies=[Depends(RateLimiter(interval_seconds=limiter_restores.seconds,
                                      max_requests=limiter_restores.max_request))],
    response_model=SuccessfulRequest,
    responses=common_error_authenticated_response,
    status_code=status.HTTP_200_OK)
@handle_exceptions_endpoint
async def delete_download_request(request: DeleteResourceRequestSchema):
    return await delete_download_request_handler(request)


# ------------------------------------------------------------------------------------------------
#             DELETE DELETE-BACKUP-REQUEST
# ------------------------------------------------------------------------------------------------


limiter_restores = endpoint_limiter.get_limiter_cust("delete_backup_request")
route = '/delete-backup-request'


@router.delete(
    path=route,
    tags=[tag_name],
    summary='Delete delete-backup-request',
    description=route_description(tag=tag_name,
                                  route=route,
                                  limiter_calls=limiter_restores.max_request,
                                  limiter_seconds=limiter_restores.seconds),
    dependencies=[Depends(RateLimiter(interval_seconds=limiter_restores.seconds,
                                      max_requests=limiter_restores.max_request))],
    response_model=SuccessfulRequest,
    responses=common_error_authenticated_response,
    status_code=status.HTTP_200_OK)
@handle_exceptions_endpoint
async def delete_delete_backup_request(request: DeleteResourceRequestSchema):
    return await delete_delete_backup_request_handler(request)
