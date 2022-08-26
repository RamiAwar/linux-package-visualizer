export function respond(body) {
	if (body.errors) {
		return { status: 401, body };
	}

	let headers = {};

	return {
		status: 200,
		headers: headers,
		body
	};
}
