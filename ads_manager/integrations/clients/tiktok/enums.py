import enum

from ads_manager import enums as source_enums


class ServiceType(enum.Enum):
    AUCTION = "AUCTION"
    RESERVATION = "RESERVATION"


class ReportType(enum.Enum):
    AUCTION = "AUCTION"
    BASIC = "BASIC"


class DataLevel(enum.Enum):
    AUCTION_CAMPAIGN = "AUCTION_CAMPAIGN"
    AUCTION_ADGROUP = "AUCTION_ADGROUP"
    AUCTION_AD = "AUCTION_AD"
    RESERVATION_CAMPAIGN = "RESERVATION_CAMPAIGN"
    RESERVATION_ADGROUP = "RESERVATION_ADGROUP"
    RESERVATION_AD = "RESERVATION_AD"

    @staticmethod
    def from_service_and_resource_type(
        service_type: ServiceType, resource_type: source_enums.ResourceType
    ) -> "DataLevel":
        return {
            ServiceType.AUCTION: {
                source_enums.ResourceType.CAMPAIGN: DataLevel.AUCTION_CAMPAIGN,
                source_enums.TiktokResourceType.AD_GROUP: DataLevel.AUCTION_ADGROUP,
                source_enums.ResourceType.AD: DataLevel.AUCTION_AD,
            },
            ServiceType.RESERVATION: {
                source_enums.ResourceType.CAMPAIGN: DataLevel.RESERVATION_CAMPAIGN,
                source_enums.TiktokResourceType.AD_GROUP: DataLevel.RESERVATION_ADGROUP,
                source_enums.ResourceType.AD: DataLevel.RESERVATION_AD,
            },
        }[service_type][resource_type]
