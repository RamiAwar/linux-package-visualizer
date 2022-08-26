import * as api from '$lib/api.js';

export async function load() {
	const packages = await api.get(`/all`);
	return packages;
}
