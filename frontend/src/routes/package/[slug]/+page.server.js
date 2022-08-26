import * as api from '$lib/api.js';

export async function load({ params }) {
	const package_data = await api.get(`/package/${params.slug}`);
	return { package_data };
}
