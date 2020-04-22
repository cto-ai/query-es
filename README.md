![](https://cto.ai/static/oss-banner.png)

# Query-ES Op 🚀

The Query ElasticSearch Op is designed to allow users to conveniently make queries to an ElasticSearch cloud.

## Requirements
To run this or any other Op, install [The Ops Platform](https://cto.ai/platform).

You can find information on how to run and build Ops via [The Ops Platform Documentation](https://cto.ai/docs/overview).

To learn more about ElasticSearch, you can find their site [here](https://www.elastic.co/).

## Usage
In Slack, you can run this Op with:

```bash
/ops run cto.ai/query-es
```
Alternatively, you can run this Op in the command line with:

```bash
ops run @cto.ai/query-es
```
The Op first requests the URL of the ElasticSearch Cloud the user wishes to query.  The user can then freely add any query body, header, or parameters to refine their query.

After making a successful query, the Op will present the following two options: printing for readability and printing for usability.

Printing for readability will have the Op indent the rows from the query result as appropriate.  To avoid printing an unexpected dump, the Op provides the option to print a short preview as well as the entire result.  The Op will inform the user of the number of lines printed in both cases.

Printing for usability will simply print the entire query result unformatted.  If the user is running the Op in Slack, the Op will break the result into 2800 character sections to conform with Slack's message size limits.  This option is intended for users who simply want to copy and paste the result.

## Debugging Issues
When submitting issues or requesting help, be sure to also include the version information. To get your Ops version run:

```bash
ops -v
```
You can reach us at the [CTO.ai Community Slack](https://cto-ai-community.slack.com/) or email us at support@cto.ai.

## Limitations & Future Improvements
Currently, there is no option to save any outputs directly through the Op.  This is due to the limited permissions the Ops Slack app requests, but may change in the future.

## Contributing
See the [Contributing Docs](CONTRIBUTING.md) for more information.

## Contributors
- **Ivan Lan** via [GitHub](https://github.com/ivanl22)

## LICENSE
[MIT](LICENSE)
