"""Deprecated. See :doc:`/examples/high_availability`."""

import warnings

from pymongo import mongo_client


class MongoReplicaSetClient(mongo_client.MongoClient):
    """Deprecated alias for :class:`~pymongo.mongo_client.MongoClient`.

    :class:`~pymongo.mongo_replica_set_client.MongoReplicaSetClient`
    will be removed in a future version of PyMongo.

    .. versionchanged:: 3.0
       :class:`~pymongo.mongo_client.MongoClient` is now the one and only
       client class for a standalone server, mongos, or replica set.
       It includes the functionality that had been split into
       :class:`~pymongo.mongo_replica_set_client.MongoReplicaSetClient`: it
       can connect to a replica set, discover all its members, and monitor
       the set for stepdowns, elections, and reconfigs.

       The ``refresh`` method is removed from
       :class:`~pymongo.mongo_replica_set_client.MongoReplicaSetClient`,
       as are the ``seeds`` and ``hosts`` properties.
    """

    def __init__(self, *args, **kwargs):
        warnings.warn(
            "MongoReplicaSetClient is deprecated, use MongoClient"
            " to connect to a replica set",
            DeprecationWarning,
            stacklevel=2,
        )

        super(MongoReplicaSetClient, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "MongoReplicaSetClient(%s)" % (self._repr_helper(),)
