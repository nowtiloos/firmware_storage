from app.interfaces.unit_of_work import IUnitOfWork


class ModifiedFirmwareServices:

    def __init__(self, unit_of_work: IUnitOfWork) -> None:
        self.unit_of_work = unit_of_work

    async def search_all_firmwares(self):
        async with self.unit_of_work as uow:
            return await uow.firmwares_repository.find_all()